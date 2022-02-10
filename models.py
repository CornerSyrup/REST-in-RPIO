import json
import os


class JsonEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


class Config:
    devices: list
    """List of registered devices"""

    def __init__(self, file="config.json") -> None:
        self.load_config(file)

    def save_config(self, file="config.json") -> None:
        src = os.getenv("RIR_CONFIG", file)
        data = json.dumps(self, cls=JsonEncoder, indent=2)
        print(data)
        open(src, "w").write(data)

    def load_config(self, file="config.json") -> None:
        src = os.getenv("RIR_CONFIG", file)
        try:
            data = json.load(open(src, "r"))
            self.devices = list(Device(**d) for d in data["devices"])
        except json.JSONDecodeError:
            self.devices = []


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
