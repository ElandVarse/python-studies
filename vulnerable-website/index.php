<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Site Vulnerável</title>
</head>
<body>
    <h1>Login</h1>
    <form action="login.php" method="post">
        Usuário: <input type="text" name="username"><br><br>
        Senha: <input type="password" name="password"><br><br>
        <input type="submit" value="Entrar">
    </form>

    <h1>Comentário</h1>
    <form action="comentario.php" method="post">
        Nome: <input type="text" name="nome"><br><br>
        Comentário: <textarea name="comentario"></textarea><br><br>
        <input type="submit" value="Enviar">
    </form>

    <h1>Upload de Arquivo</h1>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        Selecione um arquivo: <input type="file" name="arquivo"><br><br>
        <input type="submit" value="Enviar Arquivo">
    </form>
</body>
</html>
