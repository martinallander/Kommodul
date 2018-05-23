// Auto-generated. Do not edit!

// (in-package cringe_bot.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Lidardistances {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.forward = null;
      this.backward = null;
      this.right = null;
      this.left = null;
      this.turn_right = null;
      this.turn_left = null;
      this.distressed = null;
      this.minimum = null;
      this.limit = null;
      this.angle = null;
    }
    else {
      if (initObj.hasOwnProperty('forward')) {
        this.forward = initObj.forward
      }
      else {
        this.forward = false;
      }
      if (initObj.hasOwnProperty('backward')) {
        this.backward = initObj.backward
      }
      else {
        this.backward = false;
      }
      if (initObj.hasOwnProperty('right')) {
        this.right = initObj.right
      }
      else {
        this.right = false;
      }
      if (initObj.hasOwnProperty('left')) {
        this.left = initObj.left
      }
      else {
        this.left = false;
      }
      if (initObj.hasOwnProperty('turn_right')) {
        this.turn_right = initObj.turn_right
      }
      else {
        this.turn_right = false;
      }
      if (initObj.hasOwnProperty('turn_left')) {
        this.turn_left = initObj.turn_left
      }
      else {
        this.turn_left = false;
      }
      if (initObj.hasOwnProperty('distressed')) {
        this.distressed = initObj.distressed
      }
      else {
        this.distressed = false;
      }
      if (initObj.hasOwnProperty('minimum')) {
        this.minimum = initObj.minimum
      }
      else {
        this.minimum = new Array(360).fill(0);
      }
      if (initObj.hasOwnProperty('limit')) {
        this.limit = initObj.limit
      }
      else {
        this.limit = 0.0;
      }
      if (initObj.hasOwnProperty('angle')) {
        this.angle = initObj.angle
      }
      else {
        this.angle = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Lidardistances
    // Serialize message field [forward]
    bufferOffset = _serializer.bool(obj.forward, buffer, bufferOffset);
    // Serialize message field [backward]
    bufferOffset = _serializer.bool(obj.backward, buffer, bufferOffset);
    // Serialize message field [right]
    bufferOffset = _serializer.bool(obj.right, buffer, bufferOffset);
    // Serialize message field [left]
    bufferOffset = _serializer.bool(obj.left, buffer, bufferOffset);
    // Serialize message field [turn_right]
    bufferOffset = _serializer.bool(obj.turn_right, buffer, bufferOffset);
    // Serialize message field [turn_left]
    bufferOffset = _serializer.bool(obj.turn_left, buffer, bufferOffset);
    // Serialize message field [distressed]
    bufferOffset = _serializer.bool(obj.distressed, buffer, bufferOffset);
    // Check that the constant length array field [minimum] has the right length
    if (obj.minimum.length !== 360) {
      throw new Error('Unable to serialize array field minimum - length must be 360')
    }
    // Serialize message field [minimum]
    bufferOffset = _arraySerializer.int16(obj.minimum, buffer, bufferOffset, 360);
    // Serialize message field [limit]
    bufferOffset = _serializer.float32(obj.limit, buffer, bufferOffset);
    // Serialize message field [angle]
    bufferOffset = _serializer.int16(obj.angle, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Lidardistances
    let len;
    let data = new Lidardistances(null);
    // Deserialize message field [forward]
    data.forward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [backward]
    data.backward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [right]
    data.right = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [left]
    data.left = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [turn_right]
    data.turn_right = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [turn_left]
    data.turn_left = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [distressed]
    data.distressed = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [minimum]
    data.minimum = _arrayDeserializer.int16(buffer, bufferOffset, 360)
    // Deserialize message field [limit]
    data.limit = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [angle]
    data.angle = _deserializer.int16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 733;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cringe_bot/Lidardistances';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1bf1b94a213c6e33b539f2122a78cb26';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool forward
    bool backward
    bool right
    bool left
    bool turn_right
    bool turn_left
    bool distressed
    int16[360] minimum
    float32 limit
    int16 angle
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Lidardistances(null);
    if (msg.forward !== undefined) {
      resolved.forward = msg.forward;
    }
    else {
      resolved.forward = false
    }

    if (msg.backward !== undefined) {
      resolved.backward = msg.backward;
    }
    else {
      resolved.backward = false
    }

    if (msg.right !== undefined) {
      resolved.right = msg.right;
    }
    else {
      resolved.right = false
    }

    if (msg.left !== undefined) {
      resolved.left = msg.left;
    }
    else {
      resolved.left = false
    }

    if (msg.turn_right !== undefined) {
      resolved.turn_right = msg.turn_right;
    }
    else {
      resolved.turn_right = false
    }

    if (msg.turn_left !== undefined) {
      resolved.turn_left = msg.turn_left;
    }
    else {
      resolved.turn_left = false
    }

    if (msg.distressed !== undefined) {
      resolved.distressed = msg.distressed;
    }
    else {
      resolved.distressed = false
    }

    if (msg.minimum !== undefined) {
      resolved.minimum = msg.minimum;
    }
    else {
      resolved.minimum = new Array(360).fill(0)
    }

    if (msg.limit !== undefined) {
      resolved.limit = msg.limit;
    }
    else {
      resolved.limit = 0.0
    }

    if (msg.angle !== undefined) {
      resolved.angle = msg.angle;
    }
    else {
      resolved.angle = 0
    }

    return resolved;
    }
};

module.exports = Lidardistances;
