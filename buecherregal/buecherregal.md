## Bücherregal

36\. Bundeswettbewerb Informatik - Junioraufgabe 1

[Aufgabenstellung](buecherregal.pdf) - [Beispieldaten](beispieldaten.md) -  [Lösungshinweise](buecherregal_loesung.pdf) 

Die Aufgabenstellung enthält einen Fehler: 
Die Größe der Bücher in den Beispieldaten ist in mm angegeben, nicht in cm.

#### Python

```
def aufteilung(nr):
  
    f = open('./beispieldaten/buecherregal'+str(nr)+'.txt')

    anzFiguren = int(f.readline())
    anzBuecher = int(f.readline())

    a = [int(x) for x in f.readlines()]    # Liste mit den Bücherhöhen
    a.sort()

    regal = []
    
    abschnitt = []
    abschnitt.append(a[0])

    for i in range(1,len(a)):
        if a[i] - abschnitt[0] <= 30:
            abschnitt.append(a[i])
        else:
            regal.append(abschnitt)
            abschnitt = []
            abschnitt.append(a[i])
            
    regal.append(abschnitt)

    check = "möglich" if len(regal) <= anzFiguren+1 else "unmöglich"
    
    print(f'Beispiel {nr}:')
    print(f'Für die {anzBuecher} Bücher sind {anzFiguren} Figuren verfügbar.')
    print(f'Aufteilung {check}. Es werden {len(regal)-1} Figuren benötigt.')

    print(f"Mögliche Aufteilung mit {len(regal)-1} Figuren: ")
    for i in range(len(regal)-1):
        print(*regal[i])
        print('Figur')
    print(*regal[-1])
         
    print()

for i in range(1,7):
    aufteilung(i)

 


```

Ausgabe:

```
Beispiel 1:
Für die 11 Bücher sind 4 Figuren verfügbar.
Aufteilung möglich. Es werden 4 Figuren benötigt.
Mögliche Aufteilung mit 4 Figuren: 
168 170
Figur
202 211 229
Figur
233 254 260
Figur
272
Figur
306 307

Beispiel 2:
Für die 7 Bücher sind 2 Figuren verfügbar.
Aufteilung möglich. Es werden 2 Figuren benötigt.
Mögliche Aufteilung mit 2 Figuren: 
169 175
Figur
203 209 210 229
Figur
235

Beispiel 3:
Für die 7 Bücher sind 2 Figuren verfügbar.
Aufteilung unmöglich. Es werden 3 Figuren benötigt.
Mögliche Aufteilung mit 3 Figuren: 
170 174
Figur
202 229
Figur
235
Figur
279 305

Beispiel 4:
Für die 100 Bücher sind 4 Figuren verfügbar.
Aufteilung möglich. Es werden 4 Figuren benötigt.
Mögliche Aufteilung mit 4 Figuren: 
160 160 161 161 162 165 165 166 167 167 167 169 170 170 171 173 173 174 174 177 180 182 183 184 184 185 185 187 188 189 190
Figur
196 197 197 199 200 201 202 206 207 207 211 212 212 214 215 216 217 218 219 224 225
Figur
233 235 237 238 238 239 240 240 240 245 246 246 247 253 254 256 258 259 259 261
Figur
264 266 266 267 268 270 270 272 274 275 276 277 278 279 286 286 287 288 289 290 293 293
Figur
295 296 300 301 303 304

Beispiel 5:
Für die 100 Bücher sind 3 Figuren verfügbar.
Aufteilung möglich. Es werden 3 Figuren benötigt.
Mögliche Aufteilung mit 3 Figuren: 
160 161 161 161 162 162 162 163 163 164 164 164 164 164 165 165 165 166 167 167 168 168 168 168 169 169 170 170 171 171 171 171 172 174 174 174 174 175 175 176 176 176 176 176 177 177 178 179 180 180
Figur
201 202 202 202 203 206 206 208 209 210 211 212 216 220 220 221 221 229 230 230 230 231
Figur
232 232 233 233 235 237 238 240 241 241 241 243 243 246 248 248 250 254 257 258 260 261 261
Figur
263 264 265 265 270

Beispiel 6:
Für die 100 Bücher sind 4 Figuren verfügbar.
Aufteilung unmöglich. Es werden 5 Figuren benötigt.
Mögliche Aufteilung mit 5 Figuren: 
125
Figur
160 161 162 164 166 166 167 168 169 170 171 172 174 175 175 175 175 175 177 177 177 178 179 180
Figur
200 200 203 204 207 208 208 209 211 211 214 214 218 220 221 226 228
Figur
247 255 261 262 263 264 264
Figur
281 282 282 283 283 283 285 286 287 287 290 290 291 292 292 293 293 294 295 295 296 298 298 300 304 304 304 305 305 305 305 306 306 306 306 307 307 308 308 308 309 309 309 309 310 310 310 310
Figur
340 341 342
```