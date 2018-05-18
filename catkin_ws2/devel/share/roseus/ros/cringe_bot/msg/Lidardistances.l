;; Auto-generated. Do not edit!


(when (boundp 'cringe_bot::Lidardistances)
  (if (not (find-package "CRINGE_BOT"))
    (make-package "CRINGE_BOT"))
  (shadow 'Lidardistances (find-package "CRINGE_BOT")))
(unless (find-package "CRINGE_BOT::LIDARDISTANCES")
  (make-package "CRINGE_BOT::LIDARDISTANCES"))

(in-package "ROS")
;;//! \htmlinclude Lidardistances.msg.html


(defclass cringe_bot::Lidardistances
  :super ros::object
  :slots (_forward _backward _right _left _turn_right _turn_left _minimum _limit _angle ))

(defmethod cringe_bot::Lidardistances
  (:init
   (&key
    ((:forward __forward) nil)
    ((:backward __backward) nil)
    ((:right __right) nil)
    ((:left __left) nil)
    ((:turn_right __turn_right) nil)
    ((:turn_left __turn_left) nil)
    ((:minimum __minimum) (make-array 360 :initial-element 0 :element-type :integer))
    ((:limit __limit) 0.0)
    ((:angle __angle) 0)
    )
   (send-super :init)
   (setq _forward __forward)
   (setq _backward __backward)
   (setq _right __right)
   (setq _left __left)
   (setq _turn_right __turn_right)
   (setq _turn_left __turn_left)
   (setq _minimum __minimum)
   (setq _limit (float __limit))
   (setq _angle (round __angle))
   self)
  (:forward
   (&optional __forward)
   (if __forward (setq _forward __forward)) _forward)
  (:backward
   (&optional __backward)
   (if __backward (setq _backward __backward)) _backward)
  (:right
   (&optional __right)
   (if __right (setq _right __right)) _right)
  (:left
   (&optional __left)
   (if __left (setq _left __left)) _left)
  (:turn_right
   (&optional __turn_right)
   (if __turn_right (setq _turn_right __turn_right)) _turn_right)
  (:turn_left
   (&optional __turn_left)
   (if __turn_left (setq _turn_left __turn_left)) _turn_left)
  (:minimum
   (&optional __minimum)
   (if __minimum (setq _minimum __minimum)) _minimum)
  (:limit
   (&optional __limit)
   (if __limit (setq _limit __limit)) _limit)
  (:angle
   (&optional __angle)
   (if __angle (setq _angle __angle)) _angle)
  (:serialization-length
   ()
   (+
    ;; bool _forward
    1
    ;; bool _backward
    1
    ;; bool _right
    1
    ;; bool _left
    1
    ;; bool _turn_right
    1
    ;; bool _turn_left
    1
    ;; int16[360] _minimum
    (* 2    360)
    ;; float32 _limit
    4
    ;; int16 _angle
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _forward
       (if _forward (write-byte -1 s) (write-byte 0 s))
     ;; bool _backward
       (if _backward (write-byte -1 s) (write-byte 0 s))
     ;; bool _right
       (if _right (write-byte -1 s) (write-byte 0 s))
     ;; bool _left
       (if _left (write-byte -1 s) (write-byte 0 s))
     ;; bool _turn_right
       (if _turn_right (write-byte -1 s) (write-byte 0 s))
     ;; bool _turn_left
       (if _turn_left (write-byte -1 s) (write-byte 0 s))
     ;; int16[360] _minimum
     (dotimes (i 360)
       (write-word (elt _minimum i) s)
       )
     ;; float32 _limit
       (sys::poke _limit (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _angle
       (write-word _angle s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _forward
     (setq _forward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _backward
     (setq _backward (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _right
     (setq _right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _left
     (setq _left (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _turn_right
     (setq _turn_right (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _turn_left
     (setq _turn_left (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; int16[360] _minimum
   (dotimes (i (length _minimum))
     (setf (elt _minimum i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; float32 _limit
     (setq _limit (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _angle
     (setq _angle (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get cringe_bot::Lidardistances :md5sum-) "029a944d8a38cab9394851815b26567b")
(setf (get cringe_bot::Lidardistances :datatype-) "cringe_bot/Lidardistances")
(setf (get cringe_bot::Lidardistances :definition-)
      "bool forward
bool backward
bool right
bool left
bool turn_right
bool turn_left
int16[360] minimum
float32 limit
int16 angle
")



(provide :cringe_bot/Lidardistances "029a944d8a38cab9394851815b26567b")


