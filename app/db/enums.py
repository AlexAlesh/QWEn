from __future__ import annotations

import enum


class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    LOGIST = "logist"


class RequestStatus(str, enum.Enum):
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CANCELLED = "cancelled"


class TripStatus(str, enum.Enum):
    DRAFT = "draft"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    CORRECTED = "corrected"
    CANCELLED = "cancelled"


class CorrectionResolution(str, enum.Enum):
    CONFIRMED = "confirmed"
    RETURNED = "returned"


class LockReleaseReason(str, enum.Enum):
    USER = "user"
    TIMEOUT = "timeout"
    ADMIN = "admin"
    SAVE = "save"


class PaymentGroup(str, enum.Enum):
    CASH = "cash"
    CASHLESS = "cashless"


class BackupStatus(str, enum.Enum):
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
