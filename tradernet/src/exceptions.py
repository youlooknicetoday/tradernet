

class BadSignature(Exception):
    pass


class InstrumentNotFound(Exception):
    pass


dispatcher = {
    4: BadSignature,
    17: InstrumentNotFound
}
