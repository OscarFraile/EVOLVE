#!/bin/bash

# ===============================
# Actualización diaria GLOBAL
# ===============================

BASE_DIR="/c/Users/Oscar/OneDrive - FM4/Escritorio/EVOLVE/Data Science"
DATE=$(date +%Y-%m-%d)

echo "🚀 Iniciando actualización diaria global"
echo "📂 Directorio base: $BASE_DIR"
echo "----------------------------------------"

for dir in "$BASE_DIR"/*; do
  if [ -d "$dir/.git" ]; then
    echo ""
    echo "📦 Repositorio detectado: $(basename "$dir")"
    cd "$dir" || continue

    # ¿Hay cambios?
    if [ -z "$(git status --porcelain)" ]; then
      echo "✅ Sin cambios. Se omite."
      continue
    fi

    # Limpieza preventiva de datos
    git rm -r --cached --ignore-unmatch */99_Data/* >/dev/null 2>&1

    # Commit
    git add .
    git commit -m "Actualización diaria automática $DATE" >/dev/null 2>&1 \
      && echo "✏️ Commit creado" \
      || { echo "⚠️ No se pudo hacer commit"; continue; }

    # Push si existe origin
    if git remote | grep -q origin; then
      git push origin main >/dev/null 2>&1 \
        && echo "🚀 Push realizado" \
        || echo "❌ Error en push (revisa manualmente)"
    else
      echo "⚠️ No hay remoto 'origin'. Commit local creado."
    fi
  fi
done

echo ""
echo "🏁 Actualización diaria global finalizada"
