; Auto-generated. Do not edit!


(cl:in-package cringe_bot-msg)


;//! \htmlinclude IRdata.msg.html

(cl:defclass <IRdata> (roslisp-msg-protocol:ros-message)
  ((dist
    :reader dist
    :initarg :dist
    :type cl:float
    :initform 0.0)
   (has_forward
    :reader has_forward
    :initarg :has_forward
    :type cl:boolean
    :initform cl:nil)
   (ir_forward
    :reader ir_forward
    :initarg :ir_forward
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 64 :element-type 'cl:fixnum :initial-element 0))
   (has_right
    :reader has_right
    :initarg :has_right
    :type cl:boolean
    :initform cl:nil)
   (ir_right
    :reader ir_right
    :initarg :ir_right
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 64 :element-type 'cl:fixnum :initial-element 0)))
)

(cl:defclass IRdata (<IRdata>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <IRdata>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'IRdata)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cringe_bot-msg:<IRdata> is deprecated: use cringe_bot-msg:IRdata instead.")))

(cl:ensure-generic-function 'dist-val :lambda-list '(m))
(cl:defmethod dist-val ((m <IRdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:dist-val is deprecated.  Use cringe_bot-msg:dist instead.")
  (dist m))

(cl:ensure-generic-function 'has_forward-val :lambda-list '(m))
(cl:defmethod has_forward-val ((m <IRdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:has_forward-val is deprecated.  Use cringe_bot-msg:has_forward instead.")
  (has_forward m))

(cl:ensure-generic-function 'ir_forward-val :lambda-list '(m))
(cl:defmethod ir_forward-val ((m <IRdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:ir_forward-val is deprecated.  Use cringe_bot-msg:ir_forward instead.")
  (ir_forward m))

(cl:ensure-generic-function 'has_right-val :lambda-list '(m))
(cl:defmethod has_right-val ((m <IRdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:has_right-val is deprecated.  Use cringe_bot-msg:has_right instead.")
  (has_right m))

(cl:ensure-generic-function 'ir_right-val :lambda-list '(m))
(cl:defmethod ir_right-val ((m <IRdata>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:ir_right-val is deprecated.  Use cringe_bot-msg:ir_right instead.")
  (ir_right m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <IRdata>) ostream)
  "Serializes a message object of type '<IRdata>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'dist))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'has_forward) 1 0)) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'ir_forward))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'has_right) 1 0)) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'ir_right))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <IRdata>) istream)
  "Deserializes a message object of type '<IRdata>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'dist) (roslisp-utils:decode-single-float-bits bits)))
    (cl:setf (cl:slot-value msg 'has_forward) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:setf (cl:slot-value msg 'ir_forward) (cl:make-array 64))
  (cl:let ((vals (cl:slot-value msg 'ir_forward)))
    (cl:dotimes (i 64)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
    (cl:setf (cl:slot-value msg 'has_right) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:setf (cl:slot-value msg 'ir_right) (cl:make-array 64))
  (cl:let ((vals (cl:slot-value msg 'ir_right)))
    (cl:dotimes (i 64)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<IRdata>)))
  "Returns string type for a message object of type '<IRdata>"
  "cringe_bot/IRdata")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'IRdata)))
  "Returns string type for a message object of type 'IRdata"
  "cringe_bot/IRdata")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<IRdata>)))
  "Returns md5sum for a message object of type '<IRdata>"
  "bb41efdfb7055f64a4f92993c2b04d80")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'IRdata)))
  "Returns md5sum for a message object of type 'IRdata"
  "bb41efdfb7055f64a4f92993c2b04d80")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<IRdata>)))
  "Returns full string definition for message of type '<IRdata>"
  (cl:format cl:nil "float32 dist~%bool has_forward~%int16[64] ir_forward~%bool has_right~%int16[64] ir_right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'IRdata)))
  "Returns full string definition for message of type 'IRdata"
  (cl:format cl:nil "float32 dist~%bool has_forward~%int16[64] ir_forward~%bool has_right~%int16[64] ir_right~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <IRdata>))
  (cl:+ 0
     4
     1
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'ir_forward) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     1
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'ir_right) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <IRdata>))
  "Converts a ROS message object to a list"
  (cl:list 'IRdata
    (cl:cons ':dist (dist msg))
    (cl:cons ':has_forward (has_forward msg))
    (cl:cons ':ir_forward (ir_forward msg))
    (cl:cons ':has_right (has_right msg))
    (cl:cons ':ir_right (ir_right msg))
))
