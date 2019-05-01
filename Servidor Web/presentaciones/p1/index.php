<!DOCTYPE HTML>

<html>
   <head>
      <meta charset="UTF-8">
      <title>Tres en Raya</title>
      <link rel="stylesheet" type="text/css" href="../../layout.css" />
   </head>


   <body>
      <header id="header">
         <div style="float: left;">
            <a href="/proyecto/" title="Página principal.">
               <h1>Tres en Raya</h1>
            </a>
         </div>
         <div style="float: right;">
            <a href="/proyecto/presentaciones/p1/" title="Presentación inicial.">
               <h3>Presentación 1</h3>
            </a>
         </div>
         <div style="margin: 0 auto; width: 250px;">
            <a href="/proyecto/presentaciones/" title="Todas las presentaciones.">
               <h1>Presentaciones</h1>
            </a>
         </div>
      </header>


      <?php
      include("../../navbar.html")
      ?>


      <main>
         <div class="innertube">
            <p>
               Presentación inicial del proyecto.
            </p>

            <ul>
               <li>
                  <a href="/proyecto/presentaciones/p1/p1.pdf#view=Fit" title="Presentación inicial en pdf.">
                     Versión pdf
                  </a>
               </li>
               <li>
                  <a href="/proyecto/presentaciones/p1/p1.zip" title="Presentación inicial en Beamer LaTeX.">
                     Código fuente
                  </a>
               </li>
            </ul>
         </div>
      </main>


      <?php
      include("../../footer.html")
      ?>
   </body>
</html>
