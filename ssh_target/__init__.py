import attr

@attr.s
class SshTarget:
    host = attr.ib()
    user = attr.ib()
    port = attr.ib(default=22)

    def __str__(self):
        return '{}@{}'.format(self.user, self.host)
