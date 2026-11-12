class EmailService:

    def _connect(self):
        print('connecting to a server...')

    def _authentication(self):
        print('authenticating is correct...')

    def send_email(self):
        self._connect()
        self._authentication()
        print('sending email....')
        self._disconnect()

    def _disconnect(self):
        print('disconnecting....')

email = EmailService()

email.send_email()

#То есть абстракция заключается в том чтобы создавать 1 объединяющий метод, вместо того чтобы вызывать их поотдельности
#+ - если не использовать абстракцию и поменять какой-то 1 метод, то нужно переделать все его вызовы, абстракция эту проблему решает!

