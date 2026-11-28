from config import RESEND_API_KEY
import resend


resend.api_key = RESEND_API_KEY



def send_email(verification_code, email_id):
    
    
    response = resend.Emails.send({
        "from": "AppNest <verification@mlzsattendance.store>",
        "to": [email_id],
        "subject": f"{verification_code} is your AppNest verification code",
        "html": f"""
        <div style="font-family: Arial, Helvetica, sans-serif; max-width: 520px; margin: 30px auto; padding: 35px 25px; background: #ffffff; color: #1f2937;">

            <h1 style="font-size: 27px; font-weight: 700; color: #111827; margin-bottom: 12px;">
                Verify your email.
            </h1>

            <p style="font-size: 15px; color: #6b7280; line-height: 1.7;">
                Welcome to <strong style="color: #6366f1;">AppNest</strong>!
                We're glad you're here. Enter the verification code below
                to confirm your email address and get started.
            </p>

            <div style="margin: 32px 0; padding: 25px 15px; background: #f5f5ff; border: 1px solid #e0e7ff; border-radius: 12px; text-align: center;">

                <p style="font-size: 12px; color: #6b7280; letter-spacing: 2px; text-transform: uppercase; margin: 0 0 14px;">
                    Your verification code
                </p>

                <h1 style="font-size: 36px; letter-spacing: 10px; color: #4f46e5; margin: 0; font-weight: 700;">
                    {verification_code}
                </h1>

            </div>

            <p style="font-size: 14px; color: #6b7280; line-height: 1.7;">
                This code will expire in <strong>10 minutes</strong>.
                Please don't share it with anyone. Our team will never
                ask you for this code.
            </p>

            <div style="border-top: 1px solid #e5e7eb; margin-top: 30px; padding-top: 22px;">

                <p style="font-size: 13px; color: #9ca3af; line-height: 1.6;">
                    If you didn't request this verification code, you can
                    safely ignore this email. Someone may have entered your
                    email address by mistake.
                </p>

                <p style="font-size: 14px; color: #4b5563; margin-top: 25px;">
                    Cheers,<br>
                    <strong>The AppNest Team 💜</strong>
                </p>

                <p style="font-size: 11px; color: #b0b0b0; text-align: center; margin-top: 35px;">
                    © 2026 AppNest. All rights reserved.<br>
                    Automated message · Please do not reply
                </p>

            </div>
        </div>
        """
    })

