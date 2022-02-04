class Device:
    name: str
    """Name of the device."""
    pin: int
    """Main I/O pin for the device."""
    mode: bool
    """IO mode for the device; True for input, False for output."""
    remarks: str
    """Any remark for the device."""

    def __init__(
        self, name: str, pin: int, mode: bool = True, remarks: str = ""
    ) -> None:
        """Instantiate a device config

        Args:
            name (str): Name of the device.
            pin (int): Main I/O pin for the device.
            mode (bool, optional): IO mode for the device; True for input, False for output. Defaults to True.
            remarks (str, optional): Any remark for the device. Defaults to "".
        """
        self.name = name
        self.pin = pin
        self.mode = mode
        self.remarks = remarks
