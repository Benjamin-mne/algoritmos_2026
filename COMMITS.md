# Convención de Commits

## Formato
`tipo(scope): descripción breve` (máximo 50 caracteres en el título)

## Tipos de Commit
- `feat`: Nuevo ejercicio o funcionalidad
- `fix`: Corrección de un ejercicio resuelto
- `docs`: Cambios en documentación (README, consignas)
- `refactor`: Mejora de código sin alterar funcionalidad
- `add`: Agregar TDA o código a `common/`
- `chore`: Cambios de configuración (`.gitignore`, etc.)

## Scopes
- `tpXX`: Para cambios específicos de un TP (ej: `tp01`, `tp02`)
- `common`: Para cambios en TDAs compartidos
- `repo`: Para cambios generales del repositorio (README, .gitignore)

## Ejemplos
```
feat(tp01): agrega ejercicio 5
fix(tp02): corrige lógica de pop en pila
add(common): agrega TDA Queue
docs: actualiza README con estructura
chore: actualiza .gitignore
refactor(tp01): simplifica recursividad ej22
```

## Reglas
1. Usar **presente imperativo** en la descripción: "agrega", "corrige", "actualiza".
2. No usar punto final en el título del commit.
3. Opcional: agregar cuerpo del commit (línea en blanco después del título) para explicar el "por qué" si es complejo.
