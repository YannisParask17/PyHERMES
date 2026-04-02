import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.models.normalized_model import NormalizedJob
from app.config.settings import credentials



class EmailNotifier:
    """
    Handles Email notifications
    """

    def __init__(self, sender_email :str, 
                 password :str, 
                 receiver_email :str, 
                 smtp_server :str = "smtp.gmail.com",
                 smtp_port :int = 587):
        """
        Parameters
        ----------
        sender_email : str
            Sender email address, imported from .env file
        password : str
            Password for sender email account, imported from .env file
        receiver_email : str
            Receiver email address, imported from .env file
        smtp_server : str, optional
            SMTP server, by default "smtp.gmail.com" for gmail communication
        smtp_port : int, optional
            SMTP port number, by default 587 for gmail communication
        """
        self.sender_email = sender_email
        self.password = password
        self.receiver_email = receiver_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

        
    def notify(self, job: NormalizedJob, dummy: bool = False) -> bool: # Future improvement: job:[NormalizedJob]
        """
        Notify for new jobs 

        Parameters
        ----------
        job : NormalizedJob
            Job posting object
        dummy : bool, optional
            If True, notification is printed instead of sent to email address, by default False

        Returns
        -------
        bool
            True if notification has been sent, False in case of error
        """
        
        subject = 'Jobs found by PyHERMES!' 
        body = f'{job.title} at {job.company}'


        if dummy:
            print(f'[NOTIFICATION] {subject}, {body}')
            return True
        
        else:
            message = MIMEMultipart("alternative")
            message["Subject"] = subject
            message["From"] = self.sender_email
            message["To"] = self.receiver_email
            message.attach(MIMEText(body, "plain"))

            try:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.sender_email, self.password)
                    server.sendmail(self.sender_email, self.receiver_email, message.as_string())
                print(f"[SMTP] Notification sent for {job.title} at {job.company}")
                return True

            except:
                with Exception as e:
                    print(f'[SMTP ERROR] Unable to send notification: {e}')
                return False



if __name__ == '__main__':
    from datetime import datetime

    job = NormalizedJob(external_id='1',
                    title='Senior Development engineer',
                    company='My Company A/S',
                    location='Compenhagen',
                    country=None,
                    url='www.sample.spl',
                    description='An exciting job sample',
                    work_mode='onsite',
                    commitment='full-time',
                    employment_type = 'permanent',
                    posted_at = None,
                    fetched_at=datetime(2026,2, 17))
    
    notifier = EmailNotifier(sender_email = credentials.SENDER_EMAIL,
                             password = credentials.PASSWORD,
                             receiver_email = credentials.RECEIVER_EMAIL)
    
    notifier.notify(job=job, dummy=True)
    notifier.notify(job=job, dummy=False)
