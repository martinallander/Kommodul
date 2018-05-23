; Auto-generated. Do not edit!


(cl:in-package cringe_bot-msg)


;//! \htmlinclude Lidardistances.msg.html

(cl:defclass <Lidardistances> (roslisp-msg-protocol:ros-message)
  ((forward
    :reader forward
    :initarg :forward
    :type cl:boolean
    :initform cl:nil)
   (backward
    :reader backward
    :initarg :backward
    :type cl:boolean
    :initform cl:nil)
   (right
    :reader right
    :initarg :right
    :type cl:boolean
    :initform cl:nil)
   (left
    :reader left
    :initarg :left
    :type cl:boolean
    :initform cl:nil)
   (turn_right
    :reader turn_right
    :initarg :turn_right
    :type cl:boolean
    :initform cl:nil)
   (turn_left
    :reader turn_left
    :initarg :turn_left
    :type cl:boolean
    :initform cl:nil)
   (distressed
    :reader distressed
    :initarg :distressed
    :type cl:boolean
    :initform cl:nil)
   (minimum
    :reader minimum
    :initarg :minimum
    :type (cl:vector cl:fixnum)
   :initform (cl:make-array 360 :element-type 'cl:fixnum :initial-element 0))
   (limit
    :reader limit
    :initarg :limit
    :type cl:float
    :initform 0.0)
   (angle
    :reader angle
    :initarg :angle
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Lidardistances (<Lidardistances>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Lidardistances>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Lidardistances)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cringe_bot-msg:<Lidardistances> is deprecated: use cringe_bot-msg:Lidardistances instead.")))

(cl:ensure-generic-function 'forward-val :lambda-list '(m))
(cl:defmethod forward-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:forward-val is deprecated.  Use cringe_bot-msg:forward instead.")
  (forward m))

(cl:ensure-generic-function 'backward-val :lambda-list '(m))
(cl:defmethod backward-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:backward-val is deprecated.  Use cringe_bot-msg:backward instead.")
  (backward m))

(cl:ensure-generic-function 'right-val :lambda-list '(m))
(cl:defmethod right-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:right-val is deprecated.  Use cringe_bot-msg:right instead.")
  (right m))

(cl:ensure-generic-function 'left-val :lambda-list '(m))
(cl:defmethod left-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:left-val is deprecated.  Use cringe_bot-msg:left instead.")
  (left m))

(cl:ensure-generic-function 'turn_right-val :lambda-list '(m))
(cl:defmethod turn_right-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:turn_right-val is deprecated.  Use cringe_bot-msg:turn_right instead.")
  (turn_right m))

(cl:ensure-generic-function 'turn_left-val :lambda-list '(m))
(cl:defmethod turn_left-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:turn_left-val is deprecated.  Use cringe_bot-msg:turn_left instead.")
  (turn_left m))

(cl:ensure-generic-function 'distressed-val :lambda-list '(m))
(cl:defmethod distressed-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:distressed-val is deprecated.  Use cringe_bot-msg:distressed instead.")
  (distressed m))

(cl:ensure-generic-function 'minimum-val :lambda-list '(m))
(cl:defmethod minimum-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:minimum-val is deprecated.  Use cringe_bot-msg:minimum instead.")
  (minimum m))

(cl:ensure-generic-function 'limit-val :lambda-list '(m))
(cl:defmethod limit-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:limit-val is deprecated.  Use cringe_bot-msg:limit instead.")
  (limit m))

(cl:ensure-generic-function 'angle-val :lambda-list '(m))
(cl:defmethod angle-val ((m <Lidardistances>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cringe_bot-msg:angle-val is deprecated.  Use cringe_bot-msg:angle instead.")
  (angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Lidardistances>) ostream)
  "Serializes a message object of type '<Lidardistances>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'forward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'backward) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'right) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'left) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'turn_right) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'turn_left) 1 0)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'distressed) 1 0)) ostream)
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let* ((signed ele) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    ))
   (cl:slot-value msg 'minimum))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'limit))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'angle)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 65536) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Lidardistances>) istream)
  "Deserializes a message object of type '<Lidardistances>"
    (cl:setf (cl:slot-value msg 'forward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'backward) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'right) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'left) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'turn_right) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'turn_left) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:setf (cl:slot-value msg 'distressed) (cl:not (cl:zerop (cl:read-byte istream))))
  (cl:setf (cl:slot-value msg 'minimum) (cl:make-array 360))
  (cl:let ((vals (cl:slot-value msg 'minimum)))
    (cl:dotimes (i 360)
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:aref vals i) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'limit) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'angle) (cl:if (cl:< unsigned 32768) unsigned (cl:- unsigned 65536))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Lidardistances>)))
  "Returns string type for a message object of type '<Lidardistances>"
  "cringe_bot/Lidardistances")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Lidardistances)))
  "Returns string type for a message object of type 'Lidardistances"
  "cringe_bot/Lidardistances")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Lidardistances>)))
  "Returns md5sum for a message object of type '<Lidardistances>"
  "1bf1b94a213c6e33b539f2122a78cb26")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Lidardistances)))
  "Returns md5sum for a message object of type 'Lidardistances"
  "1bf1b94a213c6e33b539f2122a78cb26")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Lidardistances>)))
  "Returns full string definition for message of type '<Lidardistances>"
  (cl:format cl:nil "bool forward~%bool backward~%bool right~%bool left~%bool turn_right~%bool turn_left~%bool distressed~%int16[360] minimum~%float32 limit~%int16 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Lidardistances)))
  "Returns full string definition for message of type 'Lidardistances"
  (cl:format cl:nil "bool forward~%bool backward~%bool right~%bool left~%bool turn_right~%bool turn_left~%bool distressed~%int16[360] minimum~%float32 limit~%int16 angle~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Lidardistances>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     0 (cl:reduce #'cl:+ (cl:slot-value msg 'minimum) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 2)))
     4
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Lidardistances>))
  "Converts a ROS message object to a list"
  (cl:list 'Lidardistances
    (cl:cons ':forward (forward msg))
    (cl:cons ':backward (backward msg))
    (cl:cons ':right (right msg))
    (cl:cons ':left (left msg))
    (cl:cons ':turn_right (turn_right msg))
    (cl:cons ':turn_left (turn_left msg))
    (cl:cons ':distressed (distressed msg))
    (cl:cons ':minimum (minimum msg))
    (cl:cons ':limit (limit msg))
    (cl:cons ':angle (angle msg))
))
