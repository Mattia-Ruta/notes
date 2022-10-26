mattia-aa@linux-portatile:/apps/v-cars.local$ dweb
mattia-aa@linux-portatile:/apps/dweb.local$ ll
total 220
drwxrwxr-x  15 mattia-aa www-data   4096 set 26 13:10 ./
drwxr-xr-x   8 mattia-aa www-data   4096 apr 25 19:37 ../
drwxr-xr-x   2 mattia-aa www-data   4096 mag 23 13:18 assets/
-rw-rw-r--   1 mattia-aa mattia-aa  1599 set 26 13:10 composer.json
-rw-rw-r--   1 mattia-aa mattia-aa 71007 set 26 13:10 composer.lock
drwxrwxr-x   5 mattia-aa www-data   4096 set 26 13:10 dev/
drwxrwxr-x   4 mattia-aa www-data   4096 giu 29 12:39 docker/
-rw-rw-r--   1 mattia-aa mattia-aa   743 set 27 10:27 docker-compose.yml
-rw-rw-r--   1 mattia-aa www-data   1793 set 27 15:10 .env
lrwxrwxrwx   1 mattia-aa www-data      4 mag 17 15:54 .env_dweb -> .env
-rw-rw-r--   1 mattia-aa mattia-aa  1722 set 26 13:10 .env_dweb.example
drwxrwxr-x   8 mattia-aa www-data   4096 ott  6 13:15 .git/
-rw-rw-r--   1 mattia-aa www-data    423 apr  6  2022 .gitattributes
-rw-rw-r--   1 mattia-aa www-data    815 giu 29 12:39 .gitignore
-rw-rw-r--   1 mattia-aa www-data   5437 lug 22 13:25 Gruntfile.js
drwxrwxr-x   4 mattia-aa www-data   4096 apr  6  2022 https_conf/
drwxrwxr-x   3 mattia-aa www-data   4096 mag 18 16:58 .idea/
drwxrwxr-x   2 mattia-aa www-data   4096 set 21 13:09 log/
drwxr-xr-x 129 mattia-aa www-data   4096 lug 22 11:43 node_modules/
-rw-rw-r--   1 mattia-aa www-data    418 apr  6  2022 package.json
-rw-rw-r--   1 mattia-aa www-data  38916 apr  6  2022 package-lock.json
drwxrwxr-x   2 mattia-aa www-data   4096 apr  6  2022 private/
-rw-rw-r--   1 mattia-aa mattia-aa  3762 set 26 13:10 readme.md
drwxrwxr-x   2 mattia-aa www-data   4096 mag 17 17:04 util/
drwxr-xr-x  17 mattia-aa www-data   4096 set 21 10:43 vendor/
drwxrwxr-x   5 mattia-aa mattia-aa  4096 set 21 10:43 wordpress/
-rw-rw-r--   1 mattia-aa mattia-aa  6599 set 26 13:10 wp-config.php
drwxrwxr-x   6 mattia-aa www-data   4096 set 27 15:44 wp-content/
mattia-aa@linux-portatile:/apps/dweb.local$ emacs .env
mattia-aa@linux-portatile:/apps/dweb.local$ emacs
mattia-aa@linux-portatile:/apps/dweb.local$ emacs .env
mattia-aa@linux-portatile:/apps/dweb.local$ cd
mattia-aa@linux-portatile:~$ ll
total 1004
drwxr-xr-x 42 mattia-aa mattia-aa   4096 ott  6 13:29 ./
drwxr-xr-x  4 root      root        4096 apr  6  2022 ../
drwxrwxr-x  9 mattia-aa mattia-aa   4096 set 30 15:10 .atom/
-rw-r--r--  1 mattia-aa mattia-aa    808 mag 16 11:55 .bash_aliases
-rw-------  1 mattia-aa mattia-aa  30244 ott  6 13:15 .bash_history
-rw-r--r--  1 mattia-aa mattia-aa    220 apr  6  2022 .bash_logout
-rw-r--r--  1 mattia-aa mattia-aa   3863 ago  8 15:39 .bashrc
drwxrwxr-x  2 mattia-aa mattia-aa   4096 lug 28 17:47 bin/
drwxr-xr-x 32 mattia-aa mattia-aa   4096 set 28 11:53 .cache/
drwxrwxr-x  5 mattia-aa mattia-aa   4096 giu  7 15:09 .cinnamon/
drwxr-xr-x 40 mattia-aa mattia-aa   4096 ott  4 10:39 .config/
File Edit Options Buffers Tools Emacs-Lisp Help
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

;; Melpa Package List
(require 'package)
(add-to-list 'package-archives
'("melpa" . "https://melpa.org/packages/")
t)
(package-initialize)

;; Mouse mode
(xterm-mouse-mode 1)
