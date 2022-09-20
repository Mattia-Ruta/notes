# Type Guarding
Use a function to tell TypeScript that it checks a union for specific type

```typescript
function isPerson(obj: Person | Thing): obj is Person {
	return obj.type === "Person";
}
```
