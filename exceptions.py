class PreparationException(Exception):
    """Exception to be raised during a preparation stage"""
    pass


class RunningException(Exception):
    """Exception to be raised during a running stage"""
    pass


class CleaningUpException(Exception):
    """Exception to be raised during a cleaning-up stage"""
    pass
