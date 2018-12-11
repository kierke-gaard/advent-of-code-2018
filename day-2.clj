(ns advent-of-code-2018.day-2)

(defn number-of-freq?
  [counts]
  (comp
   (partial < 0)
   count
   (partial filter (comp (partial = counts) second))))

(defn two-and-three-occurrences? [id]
  ((apply juxt
          (map number-of-freq?
               (list 2 3)))
   (frequencies id)))

(defn checksum [ids]
  (reduce
   *
   (map
    count
    ((juxt
      (partial filter first)
      (partial filter second))
     (map two-and-three-occurrences? ids)))))


;; === Test ========================================

(def ids
  (map seq ["aabbb" "aa" "x" "bbb"]))

(checksum ids)
;; => 4
;; as it should be, as there are two strings with pairs and two string with triples. Multiply these frequencies makes it four.
