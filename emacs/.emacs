(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages
   (quote
    (markdown-mode dotenv-mode csv php-mode python-mode web-mode xml-format yaml-mode)))
 '(send-mail-function (quote smtpmail-send-it))
 '(smtpmail-smtp-server "smtp.mailbox.org")
 '(smtpmail-smtp-service 25))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(font-lock-doc-face ((t (:inherit font-lock-string-face :foreground "gray55"))))
 '(font-lock-keyword-face ((t (:foreground "deep sky blue"))))
 '(font-lock-string-face ((t (:foreground "goldenrod"))))
 '(font-lock-type-face ((t (:foreground "green"))))
 '(font-lock-variable-name-face ((t (:foreground "ghost white"))))
 '(php-php-tag ((t (:foreground "deep sky blue")))))

;; Save backups to /tmp
(setq backup-directory-alist `((".*" . ,"/tmp/.")))
(setq auto-save-file-name-transforms `((".*" ,"/tmp/." t)))

;; Pre-save Commands
(add-hook 'before-save-hook 'delete-trailing-whitespace)

;; Require Final Endl
(setq-default require-final-newline t)

;; Melpa Package List
(require 'package)
(add-to-list 'package-archives
   '("melpa" . "https://melpa.org/packages/")
t)
(package-initialize)

;; Mouse mode
(xterm-mouse-mode 1)
(global-set-key (kbd "<mouse-4>") 'scroll-down-line)
(global-set-key (kbd "<mouse-5>") 'scroll-up-line)
