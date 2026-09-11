var alunos = ['Alex', 'Anna', 'João'];
alunos.push('Helena'); //Método push
alunos.push('Gabriel', 'Maria'); //Inserindo múltiplos elementos

alunos[alunos.length] = 'Carla'; //Inserindo de forma dinâmica com length

alunos.splice(3, 0, 'Roberto'); //Método splice

console.log(alunos);
