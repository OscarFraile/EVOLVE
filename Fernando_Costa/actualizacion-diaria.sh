#!/bin/bash

# 1. Ajuste de la ruta base (Contenedor de todos tus proyectos)
BASE_DIR="/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science"
DATE=$(date +%Y-%m-%d)

echo "🚀 Iniciando actualización global: $DATE"
echo "----------------------------------------"

actualizar_repo() {
    local repo_path=$1
    echo "📦 Procesando: $(basename "$repo_path")"
    cd "$repo_path" || return

    # Configuración de seguridad para finales de línea
    git config core.autocrlf true

    # 1. Intentar descargar cambios previos (por si editaste algo en la web)
    # Buscamos si la rama es main o master para el pull
    local branch="main"
    git rev-parse --verify master >/dev/null 2>&1 && branch="master"
    
    git pull origin $branch --rebase >/dev/null 2>&1

    # 2. Añadir cambios locales
    git add .

    # 3. Verificar si hay cambios reales para commit
    if git diff-index --quiet HEAD --; then
        echo "✅ Sin cambios nuevos."
    else
        git commit -m "Actualización diaria $DATE"
        
        # 4. Intentar subir a la rama detectada
        if git push origin $branch; then
            echo "🚀 ¡Todo subido a GitHub ($branch)!"
        else
            echo "❌ Error al subir. Revisa manualmente."
        fi
    fi
    echo "----------------------------------------"
}

# 2. Ejecución: Busca carpetas con .git dentro de Data Science
# Usamos mindepth 2 para saltar la raíz y encontrar EVOLVE, evolve-data-python, etc.
find "$BASE_DIR" -maxdepth 2 -mindepth 2 -name ".git" | while read -r line; do
    actualizar_repo "$(dirname "$line")"
done

echo "🏁 Proceso finalizado"