from .clima import molde, resumo

molde('https://search.brave.com/search?q=clima', 'div', 'class', 'temps-current t-primary svelte-15dg5t9 desktop-heading-h1', '°', 'div', 'class', 'desktop-small-regular t-secondary line-clamp-2')
molde('https://www.tempo.com/blumenau.htm', 'span', 'class', 'dato-temperatura changeUnitT', '°')
molde('https://www.tempolimpo.com/south-america/brazil/santa-catarina/blumenau/today', 'div', 'class', 'big-current-temp', '°')
molde('https://tempo.clicrbs.com.br/sc/blumenau', 'span', 'class', 'temperature_now', '.8º')
molde('https://www.climaeradar.com.br/previsao-tempo/blumenau/11848281', 'span', 'class', 'air-temp', '°', 'div', 'class', 'body')
molde('https://tempo.folha.uol.com.br/sc/blumenau', 'div', 'class', 'c-card__detail c-card__detail--secondary', ' °C')
molde('http://accuweather.com/pt/br/blumenau/35954/weather-forecast/35954', 'div', 'class', 'temp', '°C')

resumo()
