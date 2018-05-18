
(cl:in-package :asdf)

(defsystem "cringe_bot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IRdata" :depends-on ("_package_IRdata"))
    (:file "_package_IRdata" :depends-on ("_package"))
    (:file "Lidardistances" :depends-on ("_package_Lidardistances"))
    (:file "_package_Lidardistances" :depends-on ("_package"))
    (:file "Sensordata" :depends-on ("_package_Sensordata"))
    (:file "_package_Sensordata" :depends-on ("_package"))
  ))