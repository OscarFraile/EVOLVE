#!/bin/bash

# Asegúrate de que esta ruta sea la que contiene las carpetas con .git
BASE_DIR="/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science"
DATE=$(date +%Y-%m-%d)

echo "🚀 Iniciando actualización: $DATE"
echo "----------------------------------------"

actualizar_repo() {
    local repo_path=$1
    echo "📦 Procesando: $(basename "$repo_path")"
    cd "$repo_path" || return

    # 1. Traer cambios de GitHub primero para evitar bloqueos
    git pull origin main --rebase >/dev/null 2>&1

    # 2. Añadir cambios locales
    git add .

    # 3. Verificar cambios
    if git diff-index --quiet HEAD --; then
        echo "✅ Sin cambios nuevos para subir."
    else
        git commit -m "Actualización diaria $DATE"
        
        # 4. Intentar subir
        if git push origin main; then
            echo "🚀 ¡Todo subido a GitHub!"
        else
            echo "❌ Error al subir. Revisa si hay conflictos manuales."
        fi
    fi
    echo "----------------------------------------"
}

# Busca solo en las subcarpetas de Data Science (ej: EVOLVE, evolve-data-python)
# No busca en la raíz para evitar el error de repositorios anidados
find "$BASE_DIR" -maxdepth 2 -mindepth 2 -name ".git" | while read -r line; do
    actualizar_repo "$(dirname "$line")"
done

echo "🏁 Proceso finalizado"