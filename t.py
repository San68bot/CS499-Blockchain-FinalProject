import mailtrap as mt

mail = mt.Mail(
    sender=mt.Address(email="mailtrap@demomailtrap.com", name="Mailtrap Test"),
    to=[mt.Address(email="fadil.amiruddin1@gmail.com")],
    subject="You are awesome!",
    text="Congrats for sending test email with Mailtrap!",
    html = """\
<html>
  <body>
    <p>Hi,<br>
    This is a <b>test</b> email without an attachment sent using <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/640px-International_Pok%C3%A9mon_logo.svg.png">img</img>.</p>
  </body>
</html>
"""
,
    category="Integration Test",
)

client = mt.MailtrapClient(token="ae7246c3329a055a439940d82abec717")
client.send(mail)

