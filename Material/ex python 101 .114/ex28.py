<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="pt-BR" lang="pt-BR" data-ng-app="app">
    <head>
        <!-- General Tags -->
        <title>Integrees.net</title>
        <link rel="icon" href="img/favicon.png" type="image/x-icon" />
        <link rel="shortcut icon" href="img/favicon.png" type="image/x-icon" />
        <!-- Meta Tags -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8;" />
        <meta name="robots" content="index,follow" />
        <!-- Stylesheets -->
        <link rel="stylesheet" href="css/vendor_1601930975041.css">
        <link rel="stylesheet" href="css/app_1601930975041.css">        <!-- Javascripts Libs -->
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
        <script type="text/javascript">
            // Load the Visualization API and the piechart package.
            google.load('visualization', '1.0', {
                packages: ['corechart']
            });
        </script>
        <script
            type="text/javascript"
            src="https://www.google.com/recaptcha/api.js?onload=vcRecaptchaApiLoaded&render=explicit"
            async
            defer
        ></script>
        <script src="js/vendor_1601930975041.js"></script>
        <script type="application/javascript" src="ckeditor/ckeditor.js"></script>
        <script type="application/javascript" src="ckeditor/fixEquation.js"></script>
        <script type="application/javascript" src="angular-breadcrumb/angular-breadcrumb.js"></script>
        <script src="js/app_1601930975041.js"></script>
        <script>
            (function(i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r;
                (i[r] =
                    i[r] ||
                    function() {
                        (i[r].q = i[r].q || []).push(arguments);
                    }),
                    (i[r].l = 1 * new Date());
                (a = s.createElement(o)), (m = s.getElementsByTagName(o)[0]);
                a.async = 1;
                a.src = g;
                m.parentNode.insertBefore(a, m);
            })(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');
            ga('create', 'UA-79506973-3', 'auto');
            ga('send', 'pageview');
        </script>
    </head>

    <body>
        <div class="loading-app" ng-show="isLoading">Carregando...</div>
        <div ui-view></div>
    </body>
</html>
