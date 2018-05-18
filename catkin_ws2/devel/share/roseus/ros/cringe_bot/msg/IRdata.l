;; Auto-generated. Do not edit!


(when (boundp 'cringe_bot::IRdata)
  (if (not (find-package "CRINGE_BOT"))
    (make-package "CRINGE_BOT"))
  (shadow 'IRdata (find-package "CRINGE_BOT")))
(unless (find-package "CRINGE_BOT::IRDATA")
  (make-package "CRINGE_BOT::IRDATA"))

(in-package "ROS")
;;//! \htmlinclude IRdata.msg.html


(defclass cringe_bot::IRdata
  :super ros::object
  :slots (_found _has_forward _ir_forward _has_right _ir_right ))

(defmethod cringe_bot::IRdata
  (:init
   (&key
    ((:found __found) nil)
    ((:has_forward __has_forward) nil)
    ((:ir_forward __ir_forward) (make-array 64 :initial-element 0 :element-type :integer))
    ((:has_right __has_right) nil)
    ((:ir_right __ir_right) (make-array 64 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _found __found)
   (setq _has_forward __has_forward)
   (setq _ir_forward __ir_forward)
   (setq _has_right __has_right)
   (setq _ir_right __ir_right)
   self)
  (:found
   (&optional __found)
   (if __found (setq _found __found)) _found)
  (:has_forward
   (&optional __has_forward)
   (if __has_forward (setq _has_forward __has_forward)) _has_forward)
  (:ir_forward
   (&optional __ir_forward)
   (if __ir_forward (setq _ir_forward __ir_forward)) _ir_forward)
  (:has_right
   (&optional __has_right)
   (if __has_right (setq _has_right __has_right)) _has_right)
  (:ir_right
   (&optional __ir_right)
   (if __ir_right (setq _ir_right __ir_right)) _ir_right)
  (:serialization-length
   ()
   (+
    ;; bool _found
    1
    ;; bool _has_forward
    1
    ;; int16[64] _ir_forward
    (* 2    64)
    ;; bool _has_right
    1
    ;; int16[64] _ir_right
    (* 2    64)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _found
       (if _found (write-byte -1 s) (write-byte 0 s))
     ;; bool _has_forward
       (if _has_forward (write-byte -1 s) (write-byte 0 s))
     ;; int16[64] _ir_forward
     (dotimes (i 64)
       (write-word (elt _ir_forward i) s)
       )
     ;; bool _has_right
       (if _has_right (write-byte -1 s) (write-byte 0 s))
     ;; int16[64] _ir_right
     (dotimes (i 64)
       (write-word (elt _ir_right i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _found
     (setq _found (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _has_forward
     (setq _has_forward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16[64] _ir_forward
   (dotimes (i (length _ir_forward))
     (setf (elt _ir_forward i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; bool _has_right
     (setq _has_right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16[64] _ir_right
   (dotimes (i (length _ir_right))
     (setf (elt _ir_right i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;;
   self)
  )

(setf (get cringe_bot::IRdata :md5sum-) "8078a5463687326c03d4416e72b356a7")
(setf (get cringe_bot::IRdata :datatype-) "cringe_bot/IRdata")
(setf (get cringe_bot::IRdata :definition-)
      "bool found
bool has_forward
int16[64] ir_forward
bool has_right
int16[64] ir_right
")



(provide :cringe_bot/IRdata "8078a5463687326c03d4416e72b356a7")


