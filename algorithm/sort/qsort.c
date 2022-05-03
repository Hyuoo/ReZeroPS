/*
_ACRTIMP void __cdecl qsort(
    _Inout_updates_bytes_(_NumOfElements * _SizeOfElements) void*  _Base,
    _In_                                                    size_t _NumOfElements,
    _In_                                                    size_t _SizeOfElements,
    _In_ int (__cdecl* _PtFuncCompare)(void const*, void const*)
    );
*/

void quicksort(void* Base, size_t NumOfElements, size_t SizeOfElements, int (PtFuncCompare)(void const*, void const*));

void quicksort(void* Base, size_t NumOfElements, size_t SizeOfElements, int (PtFuncCompare)(void const*, void const*)){
}
