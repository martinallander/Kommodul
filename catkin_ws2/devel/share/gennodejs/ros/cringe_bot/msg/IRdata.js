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

class IRdata {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.found = null;
      this.has_forward = null;
      this.ir_forward = null;
      this.has_right = null;
      this.ir_right = null;
    }
    else {
      if (initObj.hasOwnProperty('found')) {
        this.found = initObj.found
      }
      else {
        this.found = false;
      }
      if (initObj.hasOwnProperty('has_forward')) {
        this.has_forward = initObj.has_forward
      }
      else {
        this.has_forward = false;
      }
      if (initObj.hasOwnProperty('ir_forward')) {
        this.ir_forward = initObj.ir_forward
      }
      else {
        this.ir_forward = new Array(64).fill(0);
      }
      if (initObj.hasOwnProperty('has_right')) {
        this.has_right = initObj.has_right
      }
      else {
        this.has_right = false;
      }
      if (initObj.hasOwnProperty('ir_right')) {
        this.ir_right = initObj.ir_right
      }
      else {
        this.ir_right = new Array(64).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type IRdata
    // Serialize message field [found]
    bufferOffset = _serializer.bool(obj.found, buffer, bufferOffset);
    // Serialize message field [has_forward]
    bufferOffset = _serializer.bool(obj.has_forward, buffer, bufferOffset);
    // Check that the constant length array field [ir_forward] has the right length
    if (obj.ir_forward.length !== 64) {
      throw new Error('Unable to serialize array field ir_forward - length must be 64')
    }
    // Serialize message field [ir_forward]
    bufferOffset = _arraySerializer.int16(obj.ir_forward, buffer, bufferOffset, 64);
    // Serialize message field [has_right]
    bufferOffset = _serializer.bool(obj.has_right, buffer, bufferOffset);
    // Check that the constant length array field [ir_right] has the right length
    if (obj.ir_right.length !== 64) {
      throw new Error('Unable to serialize array field ir_right - length must be 64')
    }
    // Serialize message field [ir_right]
    bufferOffset = _arraySerializer.int16(obj.ir_right, buffer, bufferOffset, 64);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type IRdata
    let len;
    let data = new IRdata(null);
    // Deserialize message field [found]
    data.found = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [has_forward]
    data.has_forward = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [ir_forward]
    data.ir_forward = _arrayDeserializer.int16(buffer, bufferOffset, 64)
    // Deserialize message field [has_right]
    data.has_right = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [ir_right]
    data.ir_right = _arrayDeserializer.int16(buffer, bufferOffset, 64)
    return data;
  }

  static getMessageSize(object) {
    return 259;
  }

  static datatype() {
    // Returns string type for a message object
    return 'cringe_bot/IRdata';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8078a5463687326c03d4416e72b356a7';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool found
    bool has_forward
    int16[64] ir_forward
    bool has_right
    int16[64] ir_right
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new IRdata(null);
    if (msg.found !== undefined) {
      resolved.found = msg.found;
    }
    else {
      resolved.found = false
    }

    if (msg.has_forward !== undefined) {
      resolved.has_forward = msg.has_forward;
    }
    else {
      resolved.has_forward = false
    }

    if (msg.ir_forward !== undefined) {
      resolved.ir_forward = msg.ir_forward;
    }
    else {
      resolved.ir_forward = new Array(64).fill(0)
    }

    if (msg.has_right !== undefined) {
      resolved.has_right = msg.has_right;
    }
    else {
      resolved.has_right = false
    }

    if (msg.ir_right !== undefined) {
      resolved.ir_right = msg.ir_right;
    }
    else {
      resolved.ir_right = new Array(64).fill(0)
    }

    return resolved;
    }
};

module.exports = IRdata;
