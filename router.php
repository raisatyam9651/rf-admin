<?php
// Local development router for PHP built-in server (php -S localhost:8080 router.php)
$uri = urldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));

// Serve static assets directly if file exists
if ($uri !== '/' && file_exists(__DIR__ . $uri)) {
    return false;
}

// Strip leading slash
$slug = ltrim($uri, '/');

// Root route
if ($slug === '' || $slug === 'index' || $slug === 'index.php') {
    include __DIR__ . '/index.php';
    exit();
}

// Clean extensionless URL mapping to .php file
if (file_exists(__DIR__ . '/' . $slug . '.php')) {
    include __DIR__ . '/' . $slug . '.php';
    exit();
}

// Direct .php file access
if (substr($slug, -4) === '.php' && file_exists(__DIR__ . '/' . $slug)) {
    include __DIR__ . '/' . $slug;
    exit();
}

// Blog directory handling
if (strpos($slug, 'blogs/') === 0 && file_exists(__DIR__ . '/' . $slug)) {
    return false;
}

// Fallback: 404
http_response_code(404);
echo "404 Not Found";
