let SearchInput         = document.getElementById('dash-search')
let Rows                = document.querySelectorAll('tbody tr')


SearchInput.addEventListener('input', () => {
    let text = SearchInput.value.toLowerCase();
    
    Rows.forEach(row => {
        let data = row.querySelectorAll('td');
        let isMatch = false;

        data.forEach(cell => {
            let cellText = cell.innerText.toLowerCase();
            if (cellText.includes(text)) {
                isMatch = true;
            }
        });

        // Update the display property based on whether there's a match
        row.style.display = isMatch ? 'table-row' : 'none';
    });
});




