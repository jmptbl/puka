# Autogenerated - do not edit

class AMQPError(Exception): pass
class AMQPSoftError(AMQPError): pass
class AMQPHardError(AMQPError): pass

class ContentTooLarge(AMQPSoftError):
    reply_code = 311
class NoRoute(AMQPSoftError):
    reply_code = 312
class NoConsumers(AMQPSoftError):
    reply_code = 313
class AccessRefused(AMQPSoftError):
    reply_code = 403
class NotFound(AMQPSoftError):
    reply_code = 404
class ResourceLocked(AMQPSoftError):
    reply_code = 405
class PreconditionFailed(AMQPSoftError):
    reply_code = 406
class ConnectionForced(AMQPHardError):
    reply_code = 320
class InvalidPath(AMQPHardError):
    reply_code = 402
class FrameError(AMQPHardError):
    reply_code = 501
class AMQPSyntaxError(AMQPHardError):
    reply_code = 502
class CommandInvalid(AMQPHardError):
    reply_code = 503
class ChannelError(AMQPHardError):
    reply_code = 504
class UnexpectedFrame(AMQPHardError):
    reply_code = 505
class ResourceError(AMQPHardError):
    reply_code = 506
class NotAllowed(AMQPHardError):
    reply_code = 530
class AMQPNotImplemented(AMQPHardError):
    reply_code = 540
class InternalError(AMQPHardError):
    reply_code = 541

ERRORS = {
    311: ContentTooLarge,
    312: NoRoute,
    313: NoConsumers,
    403: AccessRefused,
    404: NotFound,
    405: ResourceLocked,
    406: PreconditionFailed,
    320: ConnectionForced,
    402: InvalidPath,
    501: FrameError,
    502: AMQPSyntaxError,
    503: CommandInvalid,
    504: ChannelError,
    505: UnexpectedFrame,
    506: ResourceError,
    530: NotAllowed,
    540: AMQPNotImplemented,
    541: InternalError,
}
