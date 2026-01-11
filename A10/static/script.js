document.getElementById('searchForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const smiles = document.getElementById('smiles').value.trim();
    if (!smiles) {
        document.getElementById('results').innerHTML = '<div class="alert alert-error"><strong>Error:</strong> Please provide a SMILES string.</div>';
        return;
    }

    document.getElementById('results').innerHTML = '<p>Loading...</p>';

    try {
        const response = await fetch('/api/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ smiles: smiles })
        });
        const data = await response.json();
        if (data.error) {
            document.getElementById('results').innerHTML = `<div class="alert alert-error"><strong>Error:</strong> ${data.error}</div>`;
        } else {
            // Clone the template
            const template = document.getElementById('resultTemplate');
            const resultDiv = template.cloneNode(true);
            resultDiv.id = '';
            resultDiv.style.display = 'block';

            // Populate the fields
            resultDiv.querySelector('#compoundName').textContent = data.pref_name || 'Unknown Compound';
            resultDiv.querySelector('#chemblId').textContent = data.chembl_id;
            resultDiv.querySelector('#moleculeImage').src = data.image_url + '?t=' + Date.now();
            resultDiv.querySelector('#canonicalSmiles').textContent = data.canonical_smiles || 'N/A';
            resultDiv.querySelector('#formula').textContent = data.formula || 'N/A';
            resultDiv.querySelector('#molWt').textContent = data.mol_wt ? parseFloat(data.mol_wt).toFixed(2) + ' g/mol' : 'N/A';
            resultDiv.querySelector('#chemblLink').href = `https://www.ebi.ac.uk/chembl/explore/compound/${data.chembl_id}`;

            // Handle synonyms
            if (data.synonyms && data.synonyms.length > 0) {
                const synonymsContainer = resultDiv.querySelector('#synonymsContainer');
                const synonymsList = resultDiv.querySelector('#synonymsList');
                synonymsContainer.style.display = 'block';
                data.synonyms.slice(0, 10).forEach(syn => {
                    const span = document.createElement('span');
                    span.className = 'synonym-tag';
                    span.textContent = syn;
                    synonymsList.appendChild(span);
                });
                if (data.synonyms.length > 10) {
                    const span = document.createElement('span');
                    span.className = 'synonym-tag';
                    span.textContent = `+${data.synonyms.length - 10} more`;
                    synonymsList.appendChild(span);
                }
            }

            document.getElementById('results').innerHTML = '';
            document.getElementById('results').appendChild(resultDiv);
        }
    } catch (error) {
        document.getElementById('results').innerHTML = '<div class="alert alert-error"><strong>Error:</strong> Network error.</div>';
    }
});

function newSearch() {
    document.getElementById('results').innerHTML = '';
    document.getElementById('smiles').value = '';
}