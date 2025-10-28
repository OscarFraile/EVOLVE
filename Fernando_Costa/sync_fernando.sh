#!/bin/bash
# === Sincronizador automático de notebooks de Fernando ===

# --- Configuración de rutas ---
FORK_PATH="/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/evolve-data-python"
EVOLVE_PATH="/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/EVOLVE/Fernando_Costa/Notebooks"

echo "🌀 Actualizando fork desde repo original (breogann)..."
cd "$FORK_PATH" || exit
git fetch upstream
git pull upstream main
git push origin main

echo "📂 Copiando carpetas pre y post al repositorio EVOLVE..."
cp -r pre "$EVOLVE_PATH/"
cp -r post "$EVOLVE_PATH/"

echo "✅ Subiendo cambios al repo EVOLVE..."
cd "/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/EVOLVE" || exit
git add Fernando_Costa/Notebooks/
git commit -m "Sincronizar notebooks pre/post de Fernando"
git push origin main

echo "✨ Sincronización completada con éxito."
