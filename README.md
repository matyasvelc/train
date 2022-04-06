<h1>Jednokolejný vláček</h1>

<p>Cíl projektu: Chtěli jsme vytvořit jednokolejný vláček, který bude ovladatelný přes web, bude mít online kameru, plyn, brzdu, světla a klakson.</p>
<p>Co jsme udělali: Máme PID regulátor, který je schopný vyvažovat náklon vláčku, aby nespadl z kolejnice. Máme dva motory, které fungují jako plyn a brzda. Máme web s propojeným backendem a frontendem. Frontend umí backendu poslat informace, zárověň je z backendu umí číst. Máme vytisknutý model vláčku.</p>
<p>Použité technologie: Raspberry Pi 4, 3D tiskárny Průša a Ultimaker, gyroskop, akcelerometr, 2 motory, H-můstek dvoumotorový modul, čip-snímač náklonu</p>

<h3>Problémy, kterým jsme čelili:</h3>
<blockquote>
  <p>Velkým problémem bylo propojení jednotlivých zařízení, které se nám nakonec kromě frontendu s backendem webu nepovedlo.</p>
  <p>Nerozumění si s GitHubem a občasná ztráta progresu díky němu.</p>
  <p>Vyzkratování drátků při špatném zapojení.</p>
</blockquote>

<h3>Jak zprovoznit?</h3>
<p>Web</p>
  <blockquote>
  <p>Stáhněte kód a zapněte main.py.</p>
  <p>Do terminálu v frontend/src/index.js napište "npm start".</p>
  </blockquote>
<p>PID</p>
  <blockquote>
  <p>Stáhněte kód PID.</p>
  <p>Připravte si Raspberry 4, gyroskop a čip se snímačem náklonu.</p>
  <p>Zde je<a href="https://community.home-assistant.io/t/rf-reader-add-on/215938" title="Raspberry"> odkaz</a> pro připojení pinů na Raspberry 4, připojte ke snímači  náklonu a ke gyroskopu.</p>
  <p>Otevřete kód a zapněte ho.</p>
  </blockquote>
<p>Motory</p>
  <blockquote>
  <p>Stáhněte si ovládání_motorů.py.</p>
  <p>Připravte si Rapsberry 4, H-můstek a dva motory. Podle <a href="https://www.laskakit.cz/h-mustek-pro-krokovy-motor-l298n--dualni-motorovy-modul/?fbclid=IwAR0J27osccefwn7pToaFZcSSnsyBQMDsZQR1tKhF3giljvfZypOPq0dzVVA" title="Raspberry"> návodu</a> připojte motory k H-můstku. Poté podle <a href="https://linuxhint.com/gpio-pinout-raspberry-pi/?fbclid=IwAR1znVWyQl8cOaeNnZQT-NhUi1AKmjtEbqqe3JVRpIrP07jrFHfq8apKdns" title="Raspberry"> návodu</a> připojte H-můstek k Raspeberry Pi.
  <p>Po zapnutí kódu uživatel zvolí směr a jeden ze dvou motorů včetně jeho rychlosti.</p>
  </blockquote>
  
<h3>Na Projektu pracovali:</h3>
  <blockquote>
  <p>Daniel Vodička - PID</p>
  <p>Matyáš Velc - Backend webu</p>
  <p>Vojtěch Poupa - Frontend webu</p>
  <p>David Straka - Motory</p>
  <p>Ondřej Ježek - </p>
  <p>Eliška Rohlíková - Design a tisk vláčku</p>
