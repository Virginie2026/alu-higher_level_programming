#!/usr/bin/python3
"""Module that defines a class preventing new dynamic attributes."""


class LockedClass:
    """Represent a class that only allows a first_name attribute."""

    __slots__ = ["first_name"]
