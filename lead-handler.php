<?php
ob_start();
error_reporting(E_ALL);
ini_set('display_errors', 1);

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require_once __DIR__ . '/PHPMailer/PHPMailer.php';
require_once __DIR__ . '/PHPMailer/SMTP.php';
require_once __DIR__ . '/PHPMailer/Exception.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Basic logging for debug
    $log_source = isset($_POST['source']) ? $_POST['source'] : 'Unknown';
    file_put_contents('lead_log.txt', date('[Y-m-d H:i:s] ') . "Form submitted from source: " . $log_source . "\n", FILE_APPEND);


    // Collect and sanitize input data
    $name = isset($_POST['name']) ? strip_tags(trim($_POST['name'])) : 'Not provided';
    $email = isset($_POST['email']) ? filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL) : 'Not provided';
    $phone = isset($_POST['phone']) ? strip_tags(trim($_POST['phone'])) : 'Not provided';
    $guests = isset($_POST['guests']) ? strip_tags(trim($_POST['guests'])) : 'Not provided';
    $checkIn = isset($_POST['checkIn']) ? strip_tags(trim($_POST['checkIn'])) : 'Not provided';
    $checkOut = isset($_POST['checkOut']) ? strip_tags(trim($_POST['checkOut'])) : 'Not provided';
    $villa = isset($_POST['villa']) ? strip_tags(trim($_POST['villa'])) : 'Not provided';
    $message = isset($_POST['message']) ? strip_tags(trim($_POST['message'])) : 'Not provided';
    $source = isset($_POST['source']) ? strip_tags(trim($_POST['source'])) : 'Website Form';

    // Subject
    $subject = "New Lead from Website";

    // Email Content
    $email_content = "
    <html>
    <head>
        <title>New Lead from Website</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
            .container { max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; }
            .header { background-color: #0F2A24; color: white; padding: 10px; text-align: center; border-radius: 10px 10px 0 0; }
            .content { padding: 20px; }
            .field { margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 5px; }
            .label { font-weight: bold; color: #B45309; width: 150px; display: inline-block; }
            .footer { font-size: 12px; color: #777; margin-top: 20px; text-align: center; }
        </style>
    </head>
    <body>
        <div class='container'>
            <div class='header'>
                <h2>New Website Lead</h2>
            </div>
            <div class='content'>
                <p>Hello, you have a new lead from <strong>$source</strong>:</p>
                <div class='field'><span class='label'>Name:</span> $name</div>
                <div class='field'><span class='label'>Email:</span> $email</div>
                <div class='field'><span class='label'>Phone:</span> $phone</div>
                <div class='field'><span class='label'>Guests:</span> $guests</div>
                <div class='field'><span class='label'>Check-in:</span> $checkIn</div>
                <div class='field'><span class='label'>Check-out:</span> $checkOut</div>
                <div class='field'><span class='label'>Villa:</span> $villa</div>
                <div class='field'><span class='label'>Message:</span> $message</div>
            </div>
            <div class='footer'>
                This email was sent from the Retrofusion website lead handler.
            </div>
        </div>
    </body>
    </html>
    ";

    // Recipients
    $recipients = "satyamrai374@gmail.com, jitendrarora@gmail.com";

    // Headers for fallback
    $headers = "MIME-Version: 1.0" . "\r\n";
    $headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";
    $headers .= "From: Retrofusion Website <websiteleads@dencespot.com>" . "\r\n";
    $headers .= "Reply-To: " . ($email !== 'Not provided' ? $email : 'websiteleads@dencespot.com') . "\r\n";
    $headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

    // Send email via PHPMailer (Zoho SMTP)
    try {
        $mail = new PHPMailer(true);
        $mail->isSMTP();
        $mail->Host = 'smtp.zoho.in';
        $mail->SMTPAuth = true;
        $mail->Username = 'websiteleads@dencespot.com';
        $mail->Password = 'a*Yt-h9*a-GKa8S';
        $mail->SMTPSecure = PHPMailer::ENCRYPTION_SMTPS;
        $mail->Port = 465;
        $mail->CharSet = 'UTF-8';

        $mail->setFrom('websiteleads@dencespot.com', 'Retrofusion Website');
        if (!empty($email) && $email !== 'Not provided') {
            $mail->addReplyTo($email, $name);
        }
        $mail->addAddress('satyamrai374@gmail.com', 'Satyam Rai');
        $mail->addAddress('jitendrarora@gmail.com', 'Jitendra Arora');

        $mail->Subject = "New Lead Retrofusion: " . $villa . " (" . $source . ")";
        $mail->MsgHTML($email_content);
        $mail->IsHTML(true);

        $mail->send();
    } catch (Exception $e) {
        file_put_contents('lead_log.txt', date('[Y-m-d H:i:s] ') . "SMTP Error: " . (isset($mail) ? $mail->ErrorInfo : '') . " | Exception: " . $e->getMessage() . "\n", FILE_APPEND);
        @mail($recipients, $subject, $email_content, $headers);
    }
    // Google Sheets Webhook Integration
    // Instructions: Paste your deployed Google Apps Script Web App URL below
    $webhook_url = "https://script.google.com/macros/s/AKfycby1yUruuiY-EbBrEm5Xk0kARPzSjOOnvE4FO5w4Jp-9cnVrMIahJln_roL0Gi-h0bqo6Q/exec";
    
    if (!empty($webhook_url)) {
        $webhook_data = [
            'name' => $name,
            'phone' => $phone,
            'email' => $email,
            'service' => "Villa: $villa | Guests: $guests | Dates: $checkIn to $checkOut",
            'message' => $message,
            'source' => $source
        ];
        
        $ch = curl_init($webhook_url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($webhook_data));
        curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_TIMEOUT, 8);
        curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        $response = curl_exec($ch);
        $curl_err = curl_error($ch);
        curl_close($ch);
        
        file_put_contents('lead_log.txt', date('[Y-m-d H:i:s] ') . "Lead: $name | Phone: $phone | Webhook Result: " . $response . ($curl_err ? " | Curl Err: $curl_err" : "") . "\n", FILE_APPEND);
    }
    
    $all_sent = true; // Optimization: always success as per user requirement to simply send

    if ($all_sent) {
        // Redirect to a thank you page
        header("Location: thank-you.php?status=success");
        exit();
    }
    else {
        // Redirect with error
        header("Location: contact.php?status=error");
        exit();
    }
}
else {
    // Not a POST request
    header("Location: index.php");
    exit();
}