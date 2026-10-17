#!/usr/bin/env bash
# Bir komanda ilə hər iki test dəstini işə salır: API (hamısı) + UI (sabit ssenarilər).
# Məlum bug ssenariləri (known-bug) ayrıca işə salınır, çünki onların uğursuz olması gözlənilir.
# Qeyd: ortaq sandbox API tək seansda çox sorğudan sonra yavaşlaya bilər, ona görə API
# spec-ləri ayrı-ayrı və aralarında qısa fasilə ilə işə salınır.
set -u
export JAVA_TOOL_OPTIONS="-Duser.language=en -Duser.country=US -Djava.net.preferIPv4Stack=true"
cd "$(dirname "$0")"
PAUSE=${PAUSE:-45}
api=0
for spec in specs/final-project/api/*.spec; do
  echo "=== API: $spec"
  mvn test -Dgauge.specs.dir="$spec" || api=1
  sleep "$PAUSE"
done
echo "=== UI (sabit ssenarilər)"
mvn test -Dgauge.specs.dir=specs/final-project/ui -Dtags='ui & !known-bug'; ui=$?
echo "API exit code: $api | UI exit code: $ui"
exit $(( api != 0 || ui != 0 ))
