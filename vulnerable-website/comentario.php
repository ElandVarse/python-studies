<?php
$nome = $_POST['nome'];
$comentario = $_POST['comentario'];

// (Vulnerável a XSS!)
echo "<h2>Comentário Recebido:</h2>";
echo "<p><b>$nome:</b> $comentario</p>";
?>
