// Cria um objeto JavaScript
var objetoJS = { agencia: '5678-9', tipo: 'física', nome: 'Maria José', numero: '222.222-22' };

// Converte o objeto JavaScript em texto JSON
var textoJson = JSON.stringify(objetoJS);

// Armazenando os dados no navegador
localStorage.setItem('stringJSON', textoJson);
