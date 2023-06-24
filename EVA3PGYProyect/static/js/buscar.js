
    document.getElementById('searchButton').addEventListener('click', function() {
        var searchTerm = document.getElementById('searchInput').value.toLowerCase();
        var contentElements = document.getElementsByTagName('body')[0].querySelectorAll('*');
        var resultadosContainer = document.getElementById('resultadosContainer');
        resultadosContainer.innerHTML = '';

        for (var i = 0; i < contentElements.length; i++) {
            var element = contentElements[i];
            var elementText = element.innerText.toLowerCase();

            if (elementText.includes(searchTerm)) {
                var resultItem = document.createElement('p');
                var resultLink = document.createElement('a');
                resultLink.textContent = elementText;
                resultLink.href = '#' + element.id; // Enlaza al elemento usando su ID
                resultItem.appendChild(resultLink);
                resultadosContainer.appendChild(resultItem);
            }
        }

        if (resultadosContainer.children.length === 0) {
            var noResultsMessage = document.createElement('p');
            noResultsMessage.textContent = 'No se encontraron resultados.';
            resultadosContainer.appendChild(noResultsMessage);
        }
    });
