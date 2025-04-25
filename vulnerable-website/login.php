<?php
$usuario = $_POST['username'];
$senha = $_POST['password'];

// (Vulnerável a SQL Injection!)
$conn = new mysqli("localhost", "root", "", "site");

$query = "SELECT * FROM usuarios WHERE usuario = '$usuario' AND senha = '$senha'";
$result = $conn->query($query);

if ($result->num_rows > 0) {
    echo "Login bem-sucedido!";
} else {
    echo "Usuário ou senha inválidos.";
}

$conn->close();
?>
