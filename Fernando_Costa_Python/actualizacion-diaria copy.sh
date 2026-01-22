#!/bin/bash

# ===============================
# Script de actualización diaria
# ===============================

# 1️⃣ Muevete al repositorio donde tienes el fork del repo de Fernando
cd "/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/evolve-data-python" || exit

echo "🔄 Actualizando fork desde upstream..."

# 2️⃣ Trae los últimos cambios del repo original de Fernando
git fetch upstream main

# 3️⃣ Pisa toda la información del repo forkeado
git reset --hard upstream/main

# 4️⃣ Sube toda la información al repo dentro de tu GitHub
git push origin main --force

echo "📂 Copiando carpetas pre y post al repo EVOLVE..."

# 5️⃣ Sustituye las carpetas pre y post dentro de EVOLVE
cp -ru "/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/evolve-data-python/pre" "/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/EVOLVE/Fernando_Costa/Notebooks/"
cp -ru "/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/evolve-data-python/post" "/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/EVOLVE/Fernando_Costa/Notebooks/"

echo "✏️ Preparando commit en el repo EVOLVE..."

# 6️⃣ Muevete al repo propio EVOLVE
cd "/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science/EVOLVE" || exit

# 7️⃣ Añade todos los archivos
git add .

# 8️⃣ Confirma los cambios con fecha automática
git commit -m "Actualización diaria de notebooks y ejercicios personales $(date +%Y-%m-%d)"

# 9️⃣ Ejecuta los cambios en la rama main
git push origin main

echo "✅ Sincronización completa. Todos los notebooks actualizados."