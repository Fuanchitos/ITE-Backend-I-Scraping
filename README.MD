TITULO DEL DESIGN DOC
Link: Link a este design doc

Author(s): Juan Carlos Salazar Silva

Status: [In Review]

Ultima actualización: 2023-10-30

## Contenido
- Goals
- Non-Goals
- Background
- Overview
- Detailed Design
  - Scraping de Páginas del Instituto Tecnológico de Ensenada
    - Obtención de párrafos
    - Extracción de títulos
    - Recopilación de tablas
- Consideraciones
- Métricas

## Links
- [Un link](#)
- [Otro link](#)

## Objetivo
Crear un script en Python para hacer scraping en las páginas web del Instituto Tecnológico de Ensenada, extrayendo información clave como párrafos, títulos y tablas.

El objetivo es obtener datos relevantes de las páginas del Instituto para un análisis posterior o para integrar la información en otras aplicaciones.

## Goals
- Extraer párrafos informativos
- Recopilar títulos de secciones importantes
- Obtener datos estructurados de tablas específicas

## Non-Goals
- Realizar acciones invasivas en las páginas web del Instituto
- Acceder a áreas restringidas o protegidas por autenticación

## Background
El Instituto Tecnológico de Ensenada es una institución educativa con información relevante en sus páginas web. El propósito es acceder a esta información de manera automatizada para diversos propósitos, como análisis de datos o visualización.

## Overview
Para el scraping de las páginas del Instituto Tecnológico de Ensenada, se utilizará Python junto con la biblioteca BeautifulSoup para analizar la estructura HTML y obtener datos específicos como párrafos, títulos y tablas.

## Detailed Design

### Scraping de Páginas del Instituto Tecnológico de Ensenada

#### Obtención de párrafos
- Se identificarán y extraerán los párrafos informativos de las páginas relevantes del Instituto.

#### Extracción de títulos
- Se buscarán y obtendrán los títulos de las secciones importantes para comprender la estructura y el contenido de las páginas.

#### Recopilación de tablas
- Se analizarán y extraerán datos estructurados de las tablas disponibles en las páginas del Instituto.

## Consideraciones
- Respetar los términos de uso del sitio web del Instituto Tecnológico de Ensenada.
- Evitar realizar solicitudes excesivas para no sobrecargar el servidor.
- Asegurar que el scraping se realice de manera ética y legal.

## Métricas
- Tiempo requerido para el scraping de información.
- Precisión en la extracción de datos (párrafos, títulos y tablas).
