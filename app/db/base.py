from __future__ import annotations

from sqlalchemy.orm import DeclarativeBase, MappedAsOptional


class Base(DeclarativeBase):
    """Базовый класс для всех ORM-моделей DiLS."""

    type_annotation_map = {
        # Можно расширить маппинг типов при необходимости
    }


__all__ = ["Base"]
