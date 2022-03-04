class Device {
  constructor() {
    /**
     * @type String
     */
    this.name = null;
    /**
     * @type Number
     */
    this.pin = null;
    /**
     * @type String
     */
    this.remarks = null;
  }

  isValid() {
    return !!this.name && !!this.pin && this.pin >= 0;
  }
}
