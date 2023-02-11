List currently running feeds

`feeds`

Kill the processes starting with the top PID then going down

```bash
1888378    05:01:27 php -f crons/feeds/run.php robinsandday
1889173    04:59:49  \_ sh -c php crons/feeds/run.php robinsandday importStock 231366
1889174    04:59:49      \_ php crons/feeds/run.php robinsandday importStock 231366
1749818       03:09 -sh
1069803       46:26 php -f crons/feeds/run.php vcarsdna
1743839       10:46  \_ sh -c php crons/feeds/run.php vcarsdna createReports 231392
1743840       10:46      \_ php crons/feeds/run.php vcarsdna createReports 231392
```

Kill feeds

`sudo kill 1888378`

Then

`sudo kill 1889173`

`sudo kill 1889174`
