// 1. Qué son los Arrays
// 1.1 Crea una función llamada `procesarPedido` que recibe un array `pedido`.
// Debes sacar el primer elemento (nombre del cliente), añadir "bebida" al inicio del array y añadir el nombre del cliente al final.
function procesarPedido(pedido) {
    const nombreCliente = pedido.shift(); // Saca el primer elemento (nombre del cliente)
    pedido.unshift("bebida"); // Añade "bebida" al inicio
    pedido.push(nombreCliente); // Añade el nombre del cliente al final
    return pedido; // Retorna el array modificado
}

// 2. Iteración de Arrays en Javascript
// 2.1 Crea una función llamada `sumarPares` que reciba un array de números.
// Debes iterar sobre el array, sumar todos los números pares y devolver la suma.
function sumarPares(numeros) {
    let suma = 0;
    for (let numero of numeros) { // Itera sobre el array
        if (numero % 2 === 0) { // Verifica si el número es par
            suma += numero; // Suma el número a la suma total
        }
    }
    return suma; // Retorna la suma total
}

// 3. Buscar en Arrays
// 3.1 Escribe una función llamada `palabrasTerminanConA` que reciba un array de palabras y devuelva `true` si todas terminan con "a", o `false` si al menos una no lo hace.
function palabrasTerminanConA(palabras) {
    for (let palabra of palabras) { // Itera sobre el array
        if (!palabra.endsWith('a')) { // Verifica si la palabra no termina con "a"
            return false; // Si encuentra una palabra que no termina con "a", retorna false
        }
    }
    return true; // Si todas las palabras terminan con "a", retorna true
}

const palabras = ['casa', 'silla', 'mesa']
console.log(palabrasTerminanConA(palabras)) // -> true

// 4. Transformar Arrays
// 4.1 Crea una función llamada `buscaPalabras` que reciba dos parámetros: un array `words` y una palabra `word`.
// Busca el índice de la palabra en el array y devuelve todas las palabras después de ese índice en un nuevo array
function buscaPalabras(words, word) {
    const indice = words.indexOf(word); // Busca el índice de la palabra
    if (indice === -1) return []; // Si no se encuentra, retorna un array vacío
    return words.slice(indice + 1); // Retorna las palabras después del índice encontrado
}

const words = ['hola', 'mundo', 'javascript', 'node'];
console.log(buscaPalabras(words, 'mundo')) // El resultado debe ser: ['javascript', 'node']

// 5. Matrices
// 5.1 Crea una función llamada `findJavaScript` que reciba una matriz de cadenas y devuelva la posición de "JavaScript".
// Si no la encuentra, devuelve [-1, -1].
function findJavaScript(matrix) {
    for (let i = 0; i < matrix.length; i++) { // Itera sobre las filas
        for (let j = 0; j < matrix[i].length; j++) { // Itera sobre las columnas
            if (matrix[i][j] === 'JavaScript') { // Verifica si encuentra "JavaScript"
                return [i, j]; // Retorna la posición
            }
        }
    }
    return [-1, -1]; // Si no lo encuentra, retorna [-1, -1]
}

const matrix = [
    ['HTML', 'CSS', 'JavaScript'],
    ['Java', 'C++', 'Python'],
    ['Ruby', 'Go', 'Swift']
  ]
  
  const position = findJavaScript(matrix);
  console.log(position); // -> [0, 2]

// 6. Algoritmos con Arrays
// 6.1 Crea una función llamada `findMinMaxPages` que reciba un array de números (representando el número de páginas de libros).
// La función debe devolver un array con dos posiciones: el índice del libro con menos páginas y el índice del libro con más páginas.
function findMinMaxPages(books) {
    let minIndex = 0; // Índice del libro con menos páginas
    let maxIndex = 0; // Índice del libro con más páginas
    for (let i = 1; i < books.length; i++) { // Itera sobre el array
        if (books[i] < books[minIndex]) { // Encuentra el índice del libro con menos páginas
            minIndex = i;
        }
        if (books[i] > books[maxIndex]) { // Encuentra el índice del libro con más páginas
            maxIndex = i;
        }
    }
    return [minIndex, maxIndex]; // Retorna los índices
}

const libros = [350, 120, 540, 275, 390, 130, 670];
const resultado = findMinMaxPages(libros);
console.log(resultado); // -> [1, 6]

// Exportar las funciones para que puedan ser completadas y probadas
module.exports = {
    procesarPedido,
    sumarPares,
    palabrasTerminanConA,
    buscaPalabras,
    findJavaScript,
    findMinMaxPages
};
