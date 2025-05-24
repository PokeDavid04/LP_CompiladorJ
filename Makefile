# Makefile David Berrocal

# Target por defecto
all: generate

# Generar los archivos Python a partir de la gramática
generate:
	antlr4 -Dlanguage=Python3 -no-listener -visitor g.g4

# Test: ejecuta todos los archivos de prueba
test:
	@echo "Ejecutando pruebas..."
	@for file in tests/*.j; do \
		if [ -f "$$file" ]; then \
			basename=$$(basename "$$file" .j); \
			echo "Ejecutando $$basename..."; \
			python3 g.py "$$file" > "tests/$$basename.out"; \
		fi \
	done
	@echo "Pruebas completadas"

# Comparar los resultados generados con los esperados
diff:
	@echo "Comparando resultados de pruebas..."
	@for file in tests/*.j; do \
		if [ -f "$$file" ]; then \
			basename=$$(basename "$$file" .j); \
			echo "\n=== Comparando $$basename ==="; \
			if [ -f "tests/$$basename.res" ] && [ -f "tests/$$basename.out" ]; then \
				diff tests/$$basename.out tests/$$basename.res || echo ""; \
			else \
				echo "Advertencia: No se puede comparar. Falta alguno de los archivos."; \
			fi; \
			fi \
	done
	@echo "\nComparaciones completadas"

# Limpiar los archivos generados
clean:
	rm -f *.tokens
	rm -f *.interp
	rm -f g[A-Z]*.py
	rm -f __pycache__/*
	rm -rf jocs_proves/sortida

.PHONY: all generate clean test
