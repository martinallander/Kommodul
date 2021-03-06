;; Auto-generated. Do not edit!


(when (boundp 'cringe_bot::Sensordata)
  (if (not (find-package "CRINGE_BOT"))
    (make-package "CRINGE_BOT"))
  (shadow 'Sensordata (find-package "CRINGE_BOT")))
(unless (find-package "CRINGE_BOT::SENSORDATA")
  (make-package "CRINGE_BOT::SENSORDATA"))

(in-package "ROS")
;;//! \htmlinclude Sensordata.msg.html


(defclass cringe_bot::Sensordata
  :super ros::object
  :slots (_acc _angle _ir _ir_right _dist ))

(defmethod cringe_bot::Sensordata
  (:init
   (&key
    ((:acc __acc) (make-array 3 :initial-element 0.0 :element-type :float))
    ((:angle __angle) (make-array 3 :initial-element 0.0 :element-type :float))
    ((:ir __ir) (make-array 64 :initial-element 0.0 :element-type :float))
    ((:ir_right __ir_right) (make-array 64 :initial-element 0.0 :element-type :float))
    ((:dist __dist) 0.0)
    )
   (send-super :init)
   (setq _acc __acc)
   (setq _angle __angle)
   (setq _ir __ir)
   (setq _ir_right __ir_right)
   (setq _dist (float __dist))
   self)
  (:acc
   (&optional __acc)
   (if __acc (setq _acc __acc)) _acc)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:ir
   (&optional __ir)
   (if __ir (setq _ir __ir)) _ir)
  (:ir_right
   (&optional __ir_right)
   (if __ir_right (setq _ir_right __ir_right)) _ir_right)
  (:dist
   (&optional __dist)
   (if __dist (setq _dist __dist)) _dist)
  (:serialization-length
   ()
   (+
    ;; float32[3] _acc
    (* 4    3)
    ;; float32[3] _angle
    (* 4    3)
    ;; float32[64] _ir
    (* 4    64)
    ;; float32[64] _ir_right
    (* 4    64)
    ;; float32 _dist
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[3] _acc
     (dotimes (i 3)
       (sys::poke (elt _acc i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[3] _angle
     (dotimes (i 3)
       (sys::poke (elt _angle i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[64] _ir
     (dotimes (i 64)
       (sys::poke (elt _ir i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[64] _ir_right
     (dotimes (i 64)
       (sys::poke (elt _ir_right i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32 _dist
       (sys::poke _dist (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[3] _acc
   (dotimes (i (length _acc))
     (setf (elt _acc i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32[3] _angle
   (dotimes (i (length _angle))
     (setf (elt _angle i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32[64] _ir
   (dotimes (i (length _ir))
     (setf (elt _ir i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32[64] _ir_right
   (dotimes (i (length _ir_right))
     (setf (elt _ir_right i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     )
   ;; float32 _dist
     (setq _dist (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get cringe_bot::Sensordata :md5sum-) "b7176edc5b6a9cf4a3ea66544dcffbb0")
(setf (get cringe_bot::Sensordata :datatype-) "cringe_bot/Sensordata")
(setf (get cringe_bot::Sensordata :definition-)
      "float32[3] acc
float32[3] angle
float32[64] ir
float32[64] ir_right
float32 dist

")



(provide :cringe_bot/Sensordata "b7176edc5b6a9cf4a3ea66544dcffbb0")


