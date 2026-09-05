document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('item-search');
    const items = document.querySelectorAll('.js-filterable-item');
    const noResults = document.getElementById('no-results');

    if (searchInput) {
        searchInput.addEventListener('input', function () {
            const query = this.value.trim().toLowerCase();
            let visibleCount = 0;

            items.forEach((item) => {
                const name = item.dataset.name || '';
                const description = item.dataset.description || '';
                const match = name.includes(query) || description.includes(query);

                item.hidden = !match;
                if (match) visibleCount += 1;
            });

            if (noResults) {
                noResults.hidden = visibleCount !== 0;
            }
        });
    }

    const apiItemsContainer = document.getElementById('api-items');

    if (apiItemsContainer) {
        fetch('/api/items/')
            .then((response) => {
                if (!response.ok) {
                    throw new Error('No se pudieron cargar los Items desde la API');
                }
                return response.json();
            })
            .then((itemsFromApi) => {
                if (!itemsFromApi.length) {
                    apiItemsContainer.innerHTML = '<p class="empty-state">No hay items disponibles desde la API.</p>';
                    return;
                }

                apiItemsContainer.innerHTML = itemsFromApi.map((item) => `
                    <article class="item-card">
                        <div class="item-card__header">
                            <h3>${item.name}</h3>
                            <span class="item-badge">API</span>
                        </div>
                        <p>${item.description || 'Sin descripción.'}</p>
                        <small>Creado: ${item.created_at}</small>
                    </article>
                `).join('');
            })
            .catch((error) => {
                apiItemsContainer.innerHTML = `<p class="empty-state">${error.message}</p>`;
            });
    }
});
